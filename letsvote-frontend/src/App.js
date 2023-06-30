import { Route, Routes } from "react-router-dom";
import { useState, useEffect } from "react";

import Header from "./Header";
import Footer from "./Footer";
import Home from "./components/home/Home";

import Statistics from "./components/statistics/Statistics";
import Info from "./components/info/Info";
import Category from "./components/categories/Category";
import axios from "axios";

function App() {
  const [categories, setCategories] = useState([])
  const [promotions, setPromotions] = useState([])
  const [elements, setElements] = useState([])

  useEffect(() => {
    const getPromotions = async () => {
      const response = await fetch('http://127.0.0.1:8000/api/')
      let data = await response.json()
      setPromotions(data)
    }

    getPromotions()
  }, [])


  useEffect(() => {
    const getCategories = async () => {
      const response = await fetch('http://127.0.0.1:8000/api/category')
      let data = await response.json()
      setCategories(data)
    }

    getCategories()
  }, [])

  useEffect(() => {
    const getElements = async () => {
      const response = await fetch('http://127.0.0.1:8000/api/element')
      let data = await response.json()
      setElements(data)
    }

    getElements()
  }, [])

  return (
    <div className="App">
      <Header categories={categories}/>
        <Routes>
          <Route path="/" element={<Home promotions={promotions} />} />
          {categories.map((category, index) => 
          <Route key={index} path={"/category/" + category.id} element={<Category id = {category.id}/>} />
          )}
          {promotions.map((promotion, index) => 
          <Route key={index} path={"/card/"+promotion.battle} element={<Statistics id={promotion.battle} key={index}/>} />
          )}
          {elements.map((element, index) =>
          <Route key={index} path={"info/" + element.id} element={<Info id={element.id} image={element.image}/>} />
          )}
        </Routes>
      <Footer />
    </div>
  );
}

export default App;
