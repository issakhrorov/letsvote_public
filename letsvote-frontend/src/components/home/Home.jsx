import Card from "../cards/card/Card"
import React, { useState, useEffect } from "react"

const Home = ({promotions}) => {
  const [query, setQuery] = useState("")
  
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
        {promotions
          .filter((value) => {
            if (query === "") {
              return value
            } else if (
              value.battle_name.toLowerCase().includes(query.toLowerCase())
            ) {
              return value
            }
          })
            .map((promotion) => 
              <Card 
                key = {promotion.battle}
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

export default Home