import FirstChart from "./charts/FirstChart"
import messi from '../../assets/img/category_1_messi.jpeg'
import ronaldo from '../../assets/img/category_1_ronaldo.jpeg'
import { Link } from "react-router-dom"
import { 
  FaArrowUp,
} from 'react-icons/fa'
import React, { useEffect, useState} from "react"
import axios from "axios"

const Statistics = ({id}) => {

  let [battles, setBattles] = useState([])
  let [left, setLeft] = useState([])
  let [right, setRight] = useState([])

  useEffect(() => {
    getBattles()
  }, [])

  let getBattles = async () => {
    let response = await fetch('http://127.0.0.1:8000/api/card/' + id)
    let data = await response.json()
    setBattles(data)
    setLeft(data[0]['left_vote_count'])
    setRight(data[0]['right_vote_count'])
  }

  const postVote = async () => {
    const left = battles[0]['left_elem']['id']
    await axios.post(`http://localhost:8000/api/vote/`, { 'left': left })
    .then(res => {
      console.log(res);
      console.log(res.data);

      setLeft(res.data.data.left_votes_count)
      setRight(res.data.data.right_votes_count)
    })
  }

  const postRightVote = async () => {
    const right = battles[0]['right_elem']['id']
    await axios.post(`http://localhost:8000/api/rvote/`, { 'right': right })
    .then(res => {
      console.log(res);
      console.log(res.data);
      setLeft(res.data.left_votes_count)
      setRight(res.data.right_votes_count)
    })
  }
  console.log(left)
  console.log(right)

  return (
    battles.map((battle, index) => 
    <main key={index} className="Statistics">
      <div className="StatisticsVote">
        <div className="CardItem ItemOne">
          <div className="CardItemImage">
            <img src={"http://localhost:8000" + battle.left_elem.image} alt={battle.left_elem.image} />
            <p>{battle.left_elem.element_name}</p>
          </div>
          <div className="CardButtons">
            <Link to={'/info/' + battle.left_elem.id} className="InfoButton">More Info</Link>
            <Link className="VoteButton" onClick={postVote}>
              <FaArrowUp 
                className="Vote"
              />
            </Link>
          </div>
        </div>
        <FirstChart 
          left_elem={battle.left_elem.element_name}        
          right_elem={battle.right_elem.element_name}      
          left={left}
          right={right}
        />
        <div className="CardItem ItemTwo">
          <div className="CardItemImage">
            <img src={"http://localhost:8000"+ battle.right_elem.image} alt={battle.right_elem.image} />
            <p>{battle.right_elem.element_name}</p>
          </div>
          <div className="CardButtons">
            <Link className="VoteButton" onClick={postRightVote}>
              <FaArrowUp className="Vote"/>
            </Link>
            <Link to={'/info/' + battle.right_elem.id} className="InfoButton">More Info</Link>
          </div>
        </div>
      </div>

      <div className="StatisticsTable">
          <a href="">Statistics</a>
      </div>

    </main>
    )
  )
}

export default Statistics