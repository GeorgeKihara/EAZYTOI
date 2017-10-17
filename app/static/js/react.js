/*** @jsx React.DOM */

var realPython = React.createClass({
    render: function () {
        return (<h2>Hi there! We are about to create awesome stuff using react.<br></br>
            Baby steps, dont worry we'll get there with time </h2>);
    }
});

ReactDOM.render(
    React.createElement(realPython, null),
    document.getElementById('content')
);
//loader
class App extends React.Component {
    constructor() {
        super();

        this.state = {
            loading: true
        };
    }

    componentDidMount() {
        setTimeout(() => this.setState({ loading: false }), 2000);
    }

    render() {
        const { loading } = this.state;

        if (loading) {
            return null; // render null when app is not ready
        }

        return (
            <div>I'm the app</div>
        );
    }
}
ReactDOM.render(
    <App />,
      document.getElementById('app')
);