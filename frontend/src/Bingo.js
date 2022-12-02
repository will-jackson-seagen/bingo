import {
    Streamlit,
    StreamlitComponentBase,
    withStreamlitConnection,
} from "streamlit-component-lib"
import React from "react"


const Square = (text) => {
    try {
        if ((text.startsWith('http://') | text.startsWith('https://'))) {
            return (<div><img src={text} width="50%" alt="Bingo Option" /></div>)
        } else if (text.length > 100) {
            return (<div style={{ fontSize: "0.85em" }}>{text}</div>)
        } else {
            return (<div>{text}</div>)
        }
    } catch (error) {
        return (<div>Free Space!</div>)
    }
}

class Bingo extends StreamlitComponentBase {
    constructor(props) {
        super(props);
        this.state = {
            position: [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ],
            winner: false
        };
    }

    bingo() {
        console.log("BINGO!")

        // This is not needed since it is set in check_bingo()
        // this.setState(prevState => ({
        //     winner: true
        // }));

        // Method to pass back to Streamlit
        // This currently causes the Streamlit page to redraw
        Streamlit.setComponentValue(true)
    }

    check_bingo() {
        // Re-set the iframe height just because
        Streamlit.setFrameHeight()

        let is_winner = false
        let p = this.state.position

        // Check each row to see if there's a bingo
        for (let r = 0; r < 5; r++) {
            let score = 0
            for (let c = 0; c < 5; c++) {
                score += p[r][c]
            }
            if (score === 5) {
                this.bingo()
                is_winner = true
            }
        }

        // Check each column to see if there's a bingo
        for (let c = 0; c < 5; c++) {
            let score = 0
            for (let r = 0; r < 5; r++) {
                score += p[r][c]
            }
            if (score === 5) {
                this.bingo()
                is_winner = true
            }
        }

        // Check the diagonals to see if there's a bing
        if ((p[0][0] + p[1][1] + p[2][2] + p[3][3] + p[4][4]) === 5) {
            this.bingo()
            is_winner = true
        }
        if ((p[4][0] + p[3][1] + p[2][2] + p[1][3] + p[0][4]) === 5) {
            this.bingo()
            is_winner = true
        }

        // Set the winning state
        // Also used to unset the winning state
        this.setState(prevState => ({
            winner: is_winner
        }));
    }


    componentDidMount() {
        Streamlit.setComponentValue(this.props.args["value"])
        Streamlit.setFrameHeight()

        // Re-set the iframe height after 500 ms in case it didn't get set correctly the first time
        setTimeout(() => {
            Streamlit.setFrameHeight()
        }, 500);
    }


    render() {
        // Get the center piece image
        const center_piece = this.props.args["center_piece"] === undefined ? 'https://www.snowflake.com/wp-content/themes/snowflake/img/favicons/apple-touch-icon.png' : this.props.args["center_piece"]

        // Get the bingo place options
        const options = this.props.args["bingo_options"] === undefined ? ['B', 'I', 'N', 'G', 'O'] : (this.props.args["bingo_options"])

        var incr = 0
        var i = -1

        return (<>
            <table>
                <thead>
                    <tr>
                        <td>B</td>
                        <td>I</td>
                        <td>N</td>
                        <td>G</td>
                        <td>O</td>
                    </tr>
                </thead>
                <tbody>
                    {[0, 0, 0, 0, 0].map((r_val, r) => {
                        return (
                            <tr key={`r${r}`}>
                                {[0, 0, 0, 0, 0].map((c_val, c) => {
                                    i++

                                    // If the index doesn't exist, reset
                                    if (options[i] === undefined) {
                                        i = -1
                                    }
                                    incr++
                                    return (
                                        <td key={`r${r}c${c}`}>
                                            {(r === 2 & c === 2) ?
                                                <img src={center_piece} width="90%" alt="Free Space" />
                                                :
                                                <>
                                                    <input
                                                        type="checkbox"
                                                        className="btnControl"
                                                        id={`btnControl${incr}`}
                                                        onChange={(e) => {
                                                            this.state.position[r][c] = e.target.checked ? 1 : 0
                                                            this.setState(prevState => this.state.position)
                                                            this.check_bingo()
                                                        }}
                                                    />
                                                    <label className="btn" htmlFor={`btnControl${incr}`}>
                                                        <img src={center_piece} width="90%" alt="Bingo Marker" />
                                                        {Square(options[i])}
                                                    </label>
                                                </>
                                            }
                                        </td>
                                    )
                                })}
                            </tr>
                        )
                    })}
                </tbody>
            </table>
        </>)
    }
}

export default withStreamlitConnection(Bingo)