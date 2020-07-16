% include('global/header.tpl', title='Alright guvnor?')
<div class="container">
    <div class="starter-template">
        <h1>Welcome to Tiff-ictionary</h1>
        <p class="lead">
            Words are hard. British English is harder. Need to know some slang? Here is the place!
        </p>
        <p>&nbsp;</p>
        <div class="panel panel-primary">
            <div class="panel-heading">
                <h2 class="panel-title">Lookup a word or phrase</h3>
            </div>
            <div class="panel-body">
                <form class="form-inline" method="POST" action="/">
                    <fieldset>
                        <div class="form-group">
                            <input type="text" name="word" class="form-control" id="word"
                                placeholder="ceeb">
                        </div>
                        <div class="form-group">
                            <button type="submit" class="btn btn-primary">Lookup</button>
                        </div>
                    </fieldset>
                </form>
            </div>
        </div>
    </div>
</div>
% include('global/footer.tpl')