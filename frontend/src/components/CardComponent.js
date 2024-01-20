import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';

function CardComponent({id,title,img,artist}) {
  return (
    <Card style={{ width: '20rem',height:"28rem"}}>
      <Card.Img variant="top" src={img} height="300px" width="250px"/>
      <Card.Body>
        <Card.Text className='h4'>{id} {title}</Card.Text>
        <Card.Title>
          {artist}
        </Card.Title>
      </Card.Body>
    </Card>
  );
}

export default CardComponent;