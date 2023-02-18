# ArtworksGenerator
- input : Album metadata (ex. 가사 요약, 제목, 장르, 앨범 소개 등..) + 테마(ex. 일러스트, 인물, 풍경, 아이콘 등..)
- output : Album cover image

## Issue - Dataset 수집
- 10만 개 정도의 앨범 데이터가 필요한데, 한번에 request를 보내는 걸 어떻게 하는지 ?
- 많은 앨범들의 album detail data에는 **genre**가 기록되어 있지 않다. 이를 어떻게 해결할 것인지 ?
- 앨범 제목으로 할 지, 노래 제목으로 할 지

## `genius.py`
- [lyricsgenius](https://lyricsgenius.readthedocs.io/en/master/)를 이용해 노래 가사와 앨범 커버 이미지 수집
- input
    - artist name
    - song title
- output
    - song lyrics
    - album cover image