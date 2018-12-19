var query = new String();
$( document ).ready(function() {
		$( "#submit" ).click((e) => {
			query = $( "#search" ).val();
			console.log(query);
			if (query.length == 0) {
				javascript:alert('Ask me a darn question!');
			} else {
				var params = {
					FunctionName: 'getQuip',
					InvocationType: 'RequestResponse',
					LogType: 'Tail',
					Payload: '{"query": ' + JSON.stringify(query) + '}' // search terms
				};
				console.log(params);
				triggerLambda(params);
			}
		})
	});

    $( "#search" ).keypress((e) => {
    if ( e.which == 13 ) {
        $( "#submit" ).click();
    	}	
	});

function doModal(heading, formContent) {
    html =  '<div id="dynamicModal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="confirm-modal" aria-hidden="true">';
    html += '<div class="modal-dialog">';
    html += '<div class="modal-content">';
    html += '<div class="modal-header">';
    html += '<a class="close" data-dismiss="modal">X</a>';
    html += '<h4>'+heading+'</h4>'
    html += '</div>';
    html += '<div class="modal-body">';
    html += formContent;
    html += '</div>';
    html += '<div class="modal-footer">';
    html += '<span class="btn btn-primary" data-dismiss="modal">Close</span>';
    html += '</div>';  // content
    html += '</div>';  // dialog
    html += '</div>';  // footer
    html += '</div>';  // modalWindow
    $('body').append(html);
    $("#dynamicModal").modal();
    $("#dynamicModal").modal('show');

    $('#dynamicModal').on('hidden.bs.modal', function (e) {
        $(this).remove();
    });

}

function triggerLambda(params) {
	AWS.config.update({region: 'us-east-2'});
	AWS.config.credentials = new AWS.CognitoIdentityCredentials({
		IdentityPoolId: 'us-east-2:c50cc00d-7943-4e8b-b141-518f4a48ff8a',
	});

	var lambda = new AWS.Lambda({region: 'us-east-2', apiVersion: '2015-03-31'});
	var results;
	lambda.invoke(params, function(error, data) {
		if (error) {
            prompt(error);
            window.alert(JSON.parse(error));
        } else {	
			window.message = JSON.parse(data.Payload);
			console.log(message);

			if (message != null) {
				var response = message['body'];
				console.log(response);
				doModal("Uncle Paul says...",response);

			}

		}
	});

}