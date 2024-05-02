유저,상품 CRUD가 가능한 게시판 시스템 제작

![ERD](https://github.com/alluman/spartamarket_DRF/assets/160446710/f948815b-e9c4-4826-996b-a46fc42c9c5b)
/// accounts ///
회원가입 - 해당정보 기입 후 가입 가능
{
    "username": "aa",
    "email": "a@b.c",
    "password": "aa",
    "name": "aa",
    "nickname": "aa",
    "birthday": "0000-00-00",
    "gender": "Male",
    "introduction": "aaaa"
}
![회원가입](https://github.com/alluman/spartamarket_DRF/assets/160446710/743b926f-3e54-4edb-b2a3-927059dcd8cd)
로그인 - username, password 입력시 로그인 완료(토큰 포함)
![로그인](https://github.com/alluman/spartamarket_DRF/assets/160446710/c7b607dd-61b0-4991-bdcd-62fc2d08c48c)
로그아웃 - 로그인 상태 필요, RefreshToken을 blacklist에 추가
![로그아웃](https://github.com/alluman/spartamarket_DRF/assets/160446710/9d660a58-3b33-4110-b7cd-63ba939c7209)
유저프로필 - 유저 상태 확인(패스워드 제외)
![프로필](https://github.com/alluman/spartamarket_DRF/assets/160446710/eb2f87c8-06fb-4d88-a8a2-ca15bf1560f1)
유저 업데이트 - 유저 정보 변경(패스워드 제외)
![유저업데이트](https://github.com/alluman/spartamarket_DRF/assets/160446710/8d7a654f-fcf4-44b7-b90f-fd67f1e358ed)
비밀변호 수정 - old_password, new_password 입력 및 검증 후 변경
![비밀번호변경](https://github.com/alluman/spartamarket_DRF/assets/160446710/0957e954-5244-4973-8880-795e93c1d375)
유저 팔로우 - url 입력시 현재 접속중인 유저와 해당 유저가 팔로우
![팔로우](https://github.com/alluman/spartamarket_DRF/assets/160446710/14225b2c-a0f1-4a59-8923-235359dd53c2)
유저 삭제 - 비밀번호 확인 후 삭제
![유저 삭제](https://github.com/alluman/spartamarket_DRF/assets/160446710/3b8bff17-455c-4654-b602-0d2fbb6db1ae)


products
상품등록 - 해당 정보 기입 후 생성 가능
{
    "title": "a",
    "content": "sss",
    "price": 10000,
}
![상품등록](https://github.com/alluman/spartamarket_DRF/assets/160446710/b6cc2bb3-4190-4a17-8d7e-034f0609a19f)
상품목록
![상품목록](https://github.com/alluman/spartamarket_DRF/assets/160446710/8b7f6e34-6b75-4cfb-9f9b-bf93c0b46494)
상품 수정
![상품수정](https://github.com/alluman/spartamarket_DRF/assets/160446710/6101cb88-aaae-4980-a4e8-3cce425331e8)
수정 확인
![수정완료화면](https://github.com/alluman/spartamarket_DRF/assets/160446710/c83ba45f-b256-4e90-bff0-0eef1288aa55)
좋아요 / 재입력시 좋아요 취소
![좋아요](https://github.com/alluman/spartamarket_DRF/assets/160446710/3c0562ca-ecfc-4cfb-88ad-732ca30ac942)
좋아요 확인
![좋아요 1](https://github.com/alluman/spartamarket_DRF/assets/160446710/5851e2a5-f5fc-4335-a132-d33b691dcacf)
글 삭제
![삭제완료화면](https://github.com/alluman/spartamarket_DRF/assets/160446710/dfbfd78c-8793-46b1-b6b5-478a3cdb0010)
삭제 확인
![삭제완료detail](https://github.com/alluman/spartamarket_DRF/assets/160446710/303ce715-56bf-4375-820d-1462dd6c36cb)


