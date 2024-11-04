<!-- src/components/HeroSection.vue -->
<template>
    <section class="hero-section">
      <div class="hero-content">
        <h1>편리한 짐 운송 서</h1>
        <h1>스로 여행을 즐기세요</h1>
        <p>여행의 시작과 끝을 더욱 편리하게 만들어 드립니다. 저희 서비스로</p>
        <p>짐 걱정 없이 즐거운 여행을 경험하세요.</p>
        <button @click="handleBookingClick">예약하기</button>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    name: 'HeroSection',
    methods: {
      handleBookingClick() {
        // 예약하기 버튼 클릭 시 수행할 작업
        console.log('예약하기 버튼 클릭');
      },
    },
  };
  </script>
  
  <style scoped>
  /* Hero Section 전체 스타일 */
  .hero-section {
    display: flex;
    justify-content: left;
    align-items: center;
    height: 80vh;
    background-image: url('C:\movingluggage\luggage-transport-reservation\src\assets\DALL·E.webp'); /* 배경 이미지 경로 설정 */ 
    background-size: cover; /* cover 또는 contain 사용 */
    background-position: center; /* 이미지의 가운데를 기준으로 정렬 */
    color: #fff;
    text-align: center;
  }
  
  /* Hero Section 텍스트 및 버튼 스타일 */
  .hero-content h1 {
    font-size: 2.5rem;
    font-weight: bold;
    line-height: 0.5;
    /* margin-bottom: 1rem; */
  }

  
  .hero-content p {
    font-size: 1.2rem;
    line-height: 0.5;
    /* margin-bottom: 1.5rem; */
  }
  
  button {
    padding: 10px 20px;
    font-size: 1rem;
    background-color: #333;
    color: #fff;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  button:hover {
    background-color: #555;
  }
  </style>
  