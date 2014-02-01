var should = require('should');

var $body, $iframe = $('<iframe/>').appendTo('body');
describe('The homepage', function() {

    beforeEach(function(done) {
        this.timeout(10000);
        $iframe.attr('src', '/')
            .one('load', function() {
                $body = $(this.contentDocument.body);
                done();
            });
    });

    it('should render copy correctly', function() {
        $body.find('h2.top span').text().should.contain('Sustainable Crowdfunding');
        $body.find('h1 span').text().should.contain('Inspiring Generosity');
    });

    describe('Jump Box (Who inspires you?)', function() {
        it('should let you search for users through their connected accounts');
        it('should strip obviously invalid characters before submitting');
        it('should strip leading and trailing whitespace before submitting');
    });

});
