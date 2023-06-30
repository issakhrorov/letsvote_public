import { Link } from "react-router-dom"

const Card = ({
    left_elem,
    right_elem,
    battle_name,
    battle_description, 
    battle
  }) => {
  return (
    <div className="Card">
      <div className="CardImg">
        <div className="ImgOne">
          <img src={"http://localhost:8000" + left_elem} alt="" />
        </div>
        <div className="ImgTwo">
          <img src={"http://localhost:8000" + right_elem} alt="" />
        </div>
      </div>
      <div className="CardDescription">
        <h2>{battle_name}</h2>
        <p>{battle_description}</p>
        <Link to={'/card/'+battle}>Let's Vote!</Link>
      </div>
    </div>
  )
}

export default Card