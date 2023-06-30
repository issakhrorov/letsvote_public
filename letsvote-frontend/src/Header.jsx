import Navbar from "./components/navbar/Navbar"

const Header = ({categories}) => {


  return (
    <header>
      <Navbar categories={categories} />
    </header>
  )
}

export default Header