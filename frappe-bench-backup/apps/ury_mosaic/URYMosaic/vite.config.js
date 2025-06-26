import path from 'path';
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import proxyOptions from './proxyOptions';

// https://vitejs.dev/config/
export default defineConfig({
	plugins: [vue()],
	server: {
		port: 8080,
		proxy: proxyOptions
	},
	resolve: {
		alias: {
			'@': path.resolve(__dirname, 'src')
		}
	},
	build: {
		outDir: '../ury_mosaic/public/URYMosaic',
		emptyOutDir: true,
		target: 'es2015',
		// rollupOptions: {
		// 	external: ["../../assets/alert/MA_Designed_ModifiedGunBlasts_4.wav"],
		//   },
	},
});
