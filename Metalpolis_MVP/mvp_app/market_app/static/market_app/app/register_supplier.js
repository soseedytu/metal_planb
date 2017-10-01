ko.bindingHandlers.typeahead = {
    init: function (element, valueAccessor) {
        var options = ko.unwrap(valueAccessor()) || {},
            $el = $(element),
            triggerChange = function () {
                $el.change();
            };

        var displayKey = options.displayKey;
        options.displayKey = function(item) {
            return item[displayKey]();
        };
        options.dupDetector = function(remoteMatch, localMatch) {
            return false;
        };
        options.source = options.taOptions.ttAdapter();

        console.log('options local set - ', options.taOptions.ttAdapter);
        var thisTypeAhead = $el.typeahead(null, options)
        .on("typeahead:selected", triggerChange)
        .on("typeahead:autocompleted", triggerChange)
        ;

        ko.utils.domNodeDisposal.addDisposeCallback(element, function () {
            $el.typeahead("destroy");
            $el = null;
        });
    }
};

var numbers = new Bloodhound({
  datumTokenizer: function(d) {
      console.log(Bloodhound.tokenizers.whitespace(d.num));
      return Bloodhound.tokenizers.whitespace(d.num);
  },
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  local: [
    { num: 'one' },
    { num: 'two' },
    { num: 'three' },
    { num: 'four' },
    { num: 'five' },
    { num: 'six' },
    { num: 'seven' },
    { num: 'eight' },
    { num: 'nine' },
    { num: 'ten' }
  ]
});

// initialize the bloodhound suggestion engine
numbers.initialize();

// instantiate the typeahead UI
$('.typeahead').typeahead(null, {
  displayKey: 'num',
  source: numbers.ttAdapter()
});

function Option(id, name) {
    var self = this;
    self.Id = ko.observable(id);
    self.Name = ko.observable(name);
}

function viewModel() {
    var self = this;
    self.thisValue = ko.observable();
    self.someOptions = ko.observableArray([
        new Option(1, 'John'),
        new Option(2, 'Johnny'),
        new Option(3, 'Billy')
    ]);
    self.theseOptions = new Bloodhound({
      datumTokenizer: function(d) {
          var seomth = Bloodhound.tokenizers.whitespace(d.Name());
          console.log(seomth);
          return seomth },
      queryTokenizer: Bloodhound.tokenizers.whitespace,
        remote : {
            url : '%QUERY',
            transport : function(url, options, onSuccess, onError) {
                var deferred = $.Deferred();
                deferred.done( function() { onSuccess(this); });

                var filterVal = url.toLowerCase();
                var result = self.someOptions().filter( function(item) {
                    return !!~item.Name().toLowerCase().indexOf(filterVal);
                });
                deferred.resolveWith( result );
                return deferred.promise();
            }

        }
      //local: self.someOptions()
    });
    self.theseOptions.initialize();
    self.addNew = function () {
        self.someOptions.push(new Option(self.someOptions().length + 1, 'Johnnn'));
        self.theseOptions.transport.constructor.resetCache();
    }
}
ko.applyBindings(new viewModel());