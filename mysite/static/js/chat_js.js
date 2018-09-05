
var counter = 0;
    var me = {};
me.avatar = "https://lh6.googleusercontent.com/-lr2nyjhhjXw/AAAAAAAAAAI/AAAAAAAARmE/MdtfUmC0M4s/photo.jpg?sz=48";

var you = {};
you.avatar = "https://a11.t26.net/taringa/avatares/9/1/2/F/7/8/Demon_King1/48x48_5C5.jpg";

    //working code
    var chatterbotUrl = '{% url "chatterbot:chatterbot" %}';
      var csrftoken = Cookies.get('csrftoken');

      function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
      }

      $.ajaxSetup({
        beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
        }
      });

      var $chatlog = $('.js-chat-log');
      var $input = $('.js-text');
      var $sayButton = $('.js-say');

      function createRow(text, who) {
          var date = formatAMPM(new Date())
          if(who == "me"){
              //var $row = $('<li class="list-group-item"></li>');
              $row = $('<div class="chat-message clearfix">\
                 <img src="http://54.197.43.10/static/images/icon/user_icon.png" alt="" width="32" height="32">\
                  <div class="chat-message-content clearfix">\
                  <h5>{{ username }}</h5>\
                  <p id="text1">'+text+'</p>\
                  </div>\
                  </div>\
                  <hr>');
          }
          else {
               $row = $('<div class="chat-message clearfix">\
                  <img src="http://54.197.43.10/static/images/icon/usermalecircle.png" alt="" width="32" height="32">\
                  <div class="chat-message-content clearfix">\
                  <h5>John Powers</h5>\
                  <p id="text1">'+text+'</p>\
                  </div>\
                  </div>\
                  <hr>');
          }
          //$row.text(text);
          //alert(text);
          //document.getElementById("text1").innerHTML=text;
          $chatlog.append($row);
          counter++;
          document.getElementById("counter").innerHTML = counter;
      }

      function submitInput() {
        var inputData = {
          'text': $input.val()
        }

        // Display the user's input on the web page


        createRow(inputData.text, 'me');

        var $submit = $.ajax({
          type: 'POST',
          url: chatterbotUrl,
          data: JSON.stringify(inputData),
          contentType: 'application/json'
        });

        $submit.done(function(statement) {
            var result = statement.text;
            createRow(result, 'you');

            // Clear the input field
            $input.val('');

            // Scroll to the bottom of the chat interface
            $chatlog[0].scrollTop = $chatlog[0].scrollHeight;
        });

        $submit.fail(function() {
          // TODO: Handle errors
        });
      }

      $sayButton.click(function() {
        submitInput();
      });

      $input.keydown(function(event) {
        // Submit the input when the enter button is pressed
        if (event.keyCode == 13) {
          submitInput();
        }
      });


      function formatAMPM(date) {
          var hours = date.getHours();
          var minutes = date.getMinutes();
          var ampm = hours >= 12 ? 'PM' : 'AM';
          hours = hours % 12;
          hours = hours ? hours : 12; // the hour '0' should be '12'
          minutes = minutes < 10 ? '0' + minutes : minutes;
          var strTime = hours + ':' + minutes + ' ' + ampm;
          return strTime;
      }