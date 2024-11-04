<template>
  <div id="app" class="ibm-plex-sans-kr-regular">
    <AppHeader />
    <HeroSection />
    <!-- <FeaturesSection />
    <TeamSection />
    <BookingSection />
    <GallerySection />
    <ContactSection />
    <AppFooter /> -->
  </div>
</template>

<script>
import AppHeader from './components/AppHeader.vue';
import HeroSection from './components/HeroSection.vue';
// import FeaturesSection from './components/FeaturesSection.vue';
// import TeamSection from './components/TeamSection.vue';
// import BookingSection from './components/BookingSection.vue';
// import GallerySection from './components/GallerySection.vue';
// import ContactSection from './components/ContactSection.vue';
// import AppFooter from './components/AppFooter.vue';

export default {
  name: 'App',
  components: {
    AppHeader,
    HeroSection,
    // FeaturesSection,
    // TeamSection,
    // BookingSection,
    // GallerySection,
    // ContactSection,
    // AppFooter,
  },
};
</script>

<style>
html, body {
  margin: 0;
  padding: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}


</style>
