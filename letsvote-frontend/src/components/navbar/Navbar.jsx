import { Link } from "react-router-dom"
import React, { useState, useEffect } from "react"
import { 
  BiDownArrow,
  BiUpArrow
} from 'react-icons/bi'

const Navbar = ({categories}) => {  
  return (
    <nav>
      <ul className="Navbar">
        <li><Link to='/'>Let's Vote!</Link></li>
        <li>
          <a className="Categories" href="#">
            Categories <BiDownArrow />
          </a>
          <div className="DropDown">
            {categories.map((category, index) => 
              <Link to={'category/' + category.id} key={index}>{category.name}</Link>
            )} 
          </div>
        </li>
      </ul>
  </nav>
  )
}

export default Navbar