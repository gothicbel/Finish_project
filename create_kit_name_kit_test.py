# Беляков Владимир 33 когорта, Итоговый проект
import sender_stand_request
import data


def test_track_order():
    create_order = sender_stand_request.post_new_order(data.create_order_body)
    track = str(create_order.json()["track"])
    response = sender_stand_request.get_track_order(track)
    assert response.status_code == 200
