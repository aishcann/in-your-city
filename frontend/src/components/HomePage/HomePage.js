import './homepage.scss'
import eventData from '../../data.json'
import { Link } from 'react-router-dom' 

const HomePage = ({data}) => {

    console.log(data)
    return (
			<div className='homePage'>
				<section className='navbar'>
					<Link to='/login' >
                        <button>Artist Login</button>
                    </Link>
				</section>
				<section className='header'>
					<h1>In Your City</h1>
					<h3>the latest cultural events near you</h3>
				</section>
				<section className='eventList'>
					{eventData.map((event) => {
						return (
							<div className='eventInfo'>
								<img src={event.photo} alt={event.name} />
								<h3>{event.name}</h3>
								<h4>{event.date}</h4>
								<h4>{event.time}</h4>
								<h4>{event.location}</h4>
								<h4>{event.link}</h4>
								<p>{event.description}</p>
							</div>
						);
					})}
				</section>
			</div>
		);
};

export default HomePage;