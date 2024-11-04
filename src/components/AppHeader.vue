<!-- src/components/Header.vue -->
<template>
    <header class="header">
      <!-- 로고 -->
      <div class="logo">
        <h1>Logo</h1> <!-- 여기서 로고 이미지를 사용하시면 <img src="path/to/logo.png" />로 대체 -->
      </div>
      <!-- 네비게이션 메뉴 -->
      <nav class="nav-menu">
        <ul>
          <li><a href="#home">서비스 소개</a></li>
          <li><a href="#service">예약하기</a></li>
          <li><a href="#booking">고객 지원</a></li>
          <li><a href="#gallery">더보기</a></li>
        </ul>
      </nav>
      <!-- 모바일 메뉴 버튼 -->
      <div class="mobile-menu">
        <button @click="toggleMenu">☰</button>
      </div>
    </header>
  </template>
  
  <script>
  export default {
    name: 'AppHeader',
    data() {
      return {
        isMenuOpen: false, // 모바일 메뉴 열림/닫힘 상태
      };
    },
    methods: {
      toggleMenu() {
        this.isMenuOpen = !this.isMenuOpen;
      },
    },
  };
  </script>
  
  <style scoped>
/* 헤더 스타일 */
.header {
  display: flex;
  align-items: center;
  padding: 1rem 2rem;
  background-color: #fff;
  color: #fff;
}

.logo {
  font-size: 1rem;
  font-weight: bold;
  color:#000000;
  width: 100px; /* 로고 영역의 고정 너비를 설정 */
}



.nav-menu {
  flex: 1;
  display: flex;
  justify-content: center;

}

/* 네비게이션 메뉴 스타일 */
.nav-menu ul {
  display: flex;
  list-style: none;
  gap: 1rem;
  margin: 0;
  padding: 0;
}

.nav-menu a {
  color:#000000;;
  text-decoration: none;
  font-size: 1rem;
}

.nav-menu a:hover {
  text-decoration: underline;
}

/* 모바일 메뉴 버튼 스타일 */
.mobile-menu {
  display: none;
}

@media (max-width: 768px) {
  .nav-menu {
    display: none;
  }
  .mobile-menu {
    display: block;
  }
}
</style>
  