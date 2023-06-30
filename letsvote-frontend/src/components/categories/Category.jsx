import Card from "../cards/card/Card"
import React, { useState, useEffect } from "react"

const Category = ({id}) => {
  const [query, setQuery] = useState("")

  const [categoryPromotions, setCategoryPromotions] = useState([])

  useEffect(() => {
    const getCategoryPromotions = async () => {
      const response = await fetch('http://127.0.0.1:8000/api/category/' + id)
      const data = await response.json()
      setCategoryPromotions(data)
    }

    getCategoryPromotions()
  }, [])


  return (
    <main className="Home">
      <div className="Search">
        <input 
          className="SearchInput" 
          type="text" 
          placeholder="Search..."
          onChange={(e) => setQuery(e.target.value)}
        />
        <div className="SearchResults"></div>
      </div>
      <div className="Cards">
        {categoryPromotions
        .filter((value) => {
          if (query === "") {
            return value
          } else if (
            value.battle_name.toLowerCase().includes(query.toLowerCase())
          ) {
            return value
          }
        }).map((promotion, index) => 
          <Card 
            key = {index}
            left_elem = {promotion.left_elem}
            right_elem = {promotion.right_elem} 
            battle_name = {promotion.battle_name}
            battle_description = {promotion.battle_description}
            battle = {promotion.battle}
          />
        )}
      </div>
    </main>
  )
}

export default Category