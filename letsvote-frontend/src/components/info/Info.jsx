import messi from '../../assets/img/category_1_messi.jpeg'
import React, { useEffect, useState } from 'react'

const Info = ( {id, image} ) => {

  let [info, setInfo] = useState([])

  useEffect(() => {
    getInfo()
  }, [])

  let getInfo = async () => {
    let response = await fetch('http://127.0.0.1:8000/api/info/' + id)
    let data = await response.json()
    setInfo(data)
  }

  return (  
    <main>
      <article className="CardInfo">
        <div className="InfoImg">
          <img src={"http://localhost:8000" + image} alt={info.image} />
        </div>
        <div className="Info">
          <h2>{info.element_name}</h2>
          <a href="https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B8%D0%B3%D0%B3%D0%B5%D1%80_(%D0%BB%D0%BE%D1%88%D0%B0%D0%B4%D1%8C)">Материал из Википедии — свободной энциклопедии</a>
          <p>{info.description}</p>
        </div>
      </article>
    </main>
  )
}

export default Info