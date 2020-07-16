% include('global/header.tpl', title=data['name'])
<div class="container">
    <div class="starter-template">
        <div class="well well-lg">
            <h1>{{data['name']}}</h1>

            % for definition in data['definitions']:
            <p>
                <em>{{definition['type']}}</em>
                <br />
                {{definition['definition']}}
            </p>
            % end
        </div>
        
        <div class="panel panel-primary">
            <div class="panel-heading">
                <h3 class="panel-title">Need to script it?</h3>
            </div>
            <div class="panel-body">
                <p>
                Verify the results using curl:
                </p>
                <pre>curl https://dnsjson.com/{{name}}.json</pre>

                <p>
                Need the results in plain text?
                </p>
                <pre>curl https://dnsjson.com/{{name}}.txt</pre>
            </div>
        </div>
        
        <div class="panel panel-primary">
            <div class="panel-heading">
                <h3 class="panel-title">Need to lookup something else?</h3>
            </div>
            <div class="panel-body">
                <form class="form-inline" method="POST" action="/">
                    <fieldset>
                        <div class="form-group">
                            <input type="text" name="word" class="form-control" id="word"
                                placeholder="{{name}}" value="{{name}}">
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