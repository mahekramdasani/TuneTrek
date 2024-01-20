import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Row, Col } from 'react-bootstrap';
import CardComponent from './CardComponent';

const SongList = () => {
    const [songs, setSongs] = useState([]);
    const [likedSongs, setLikedSongs] = useState([]);

    useEffect(() => {
        const fetchSongs = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/songs/');
                setSongs(response.data);
            } catch (error) {
                console.error('Error fetching songs:', error);
            }
        };

        // const fetchLikedSongs = async () => {
        //     try {
        //         const response = await axios.get('http://127.0.0.1:8000/liked-songs/');
        //         setLikedSongs(response.data);
        //     } catch (error) {
        //         console.error('Error fetching liked songs:', error);
        //     }
        // };

        fetchSongs();
        // fetchLikedSongs();
    }, []);

    // const isSongLiked = (songId) => likedSongs.some(song => song.song_id === songId);

    // const likeSong = async (songId) => {
    //     try {
    //         const response = await axios.post(`http://127.0.0.1:8000/liked-songs/${songId}/`);
    //         if(response.status === 200) {
    //             setLikedSongs([...likedSongs, { id: songId }]); // Update liked songs list
    //         } else {
    //             console.error('Error liking song: Unexpected response status', response.status);
    //         }
    //     } catch (error) {
    //         console.error('Error liking song:', error);
    //     }
    // };

    // const unlikeSong = async (songId) => {
    //     try {
    //         const response = await axios.delete(`http://127.0.0.1:8000/liked-songs/${songId}/`);
    //         if(response.status === 200) {
    //             setLikedSongs(likedSongs.filter(song => song.song_id !== songId)); // Update liked songs list
    //         } else {
    //             console.error('Error unliking song: Unexpected response status', response.status);
    //         }
    //     } catch (error) {
    //         console.error('Error unliking song:', error);
    //     }
    // };
    const [searchTerm, setSearchTerm] = useState('');
    const [recommendations, setRecommendations] = useState([]);

    const handleSearchChange = (event) => {
        setSearchTerm(event.target.value);
    };

    const fetchRecommendations = async (songId) => {
        try {
            console.log(songId);
            const response = await axios.get(`http://127.0.0.1:8000/recommend-songs/${songId}/`);
            setRecommendations(response.data.slice(0, 5)); // Get only top 5 recommendations
        } catch (error) {
            console.error('Error fetching recommendations:', error);
        }
    };

    const filteredSongs = songs.filter(song => song.title.toLowerCase().includes(searchTerm.toLowerCase()));

    const CardComponentWithRecommendation = (props) => {
        return (
            <CardComponent {...props}>
                <button onClick={() => fetchRecommendations(props.id)}>Get Recommendations</button>
            </CardComponent>
        );
    };

    return (
        <div className='body'>
            <h1>Song List</h1>
            <input type="text" placeholder="Search..." onChange={handleSearchChange} />
            <Row className='container-fluid'>
                {filteredSongs.map((song) => (
                    <Col xl={3} lg={4} md={6} className='mb-3 container-fluid' key={song.song_id}>
                        <CardComponentWithRecommendation id = {song.song_id} title={song.title} img={song.image_url} artist={song.artist}/>
                        <button onClick={() => fetchRecommendations(song.song_id)}>Get Recommendations</button>
                    </Col>
                ))}
            </Row>
            <h2>Recommendations</h2>
            {recommendations.length === 0 && (
                <p>No recommendations available. Please select a song to get recommendations.</p>
            )}
            <Row className='container-fluid'>
                {recommendations.map((song) => (
                    <Col xl={3} lg={4} md={6} className='mb-3 container-fluid' key={song.song_id}>
                        <CardComponent id = {song.song_id} title={song.title} img={song.image_url} artist={song.artist}/>
                    </Col>
                ))}
            </Row>
        </div>
    );


    return (
        <div className='body'>
            <h1>Song List</h1>
            <Row className='container-fluid'>
                {songs.map((song) => (
                    <Col xl={3} lg={4} md={6} className='mb-3 container-fluid' key={song.song_id}>
                        {/* <h1 className='bg-dark'>{song.song_id}</h1> */}
                        <CardComponent id = {song.song_id} title={song.title} img={song.image_url} artist={song.artist}/>
                    </Col>
                ))}
            </Row>
        </div>
    );
};

export default SongList;
