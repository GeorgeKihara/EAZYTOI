/*** @jsx React.DOM */

var realPython = React.createClass({
    render: function() {
      return (<h2>Hi there! We are about to create awesome stuff using react.<br></br>
       Baby steps, dont worry we'll get there with time </h2>);
    }
  });

  ReactDOM.render(
    React.createElement(realPython, null),
    document.getElementById('content')
  );