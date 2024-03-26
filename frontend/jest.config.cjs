module.exports = {
  testEnvironment: 'jest-environment-jsdom',
	setupFilesAfterEnv: ["<rootDir>/tests/setupTests.ts"],
  setupFiles: ['./jest.setup.js'],
  transform: {
		"^.+\\.(js|jsx|ts|tsx)$": [
			"@swc/jest",
			{
				sourceMaps: true,
				jsc: {
					parser: {
						syntax: "typescript",
						tsx: true,
					},
					transform: {
						react: {
							runtime: "automatic",
						},
					},
				},
			},
		]
	},
	moduleNameMapper: {
		"\\.svg$": "<rootDir>/tests/svg.mock.js",
		"\\.(css|less|scss|sass)$": "identity-obj-proxy",
		"\\.(jpg|jpeg|png|gif|eot|otf|webp|ttf|woff|woff2|mp4|webm|wav|mp3|m4a|aac|oga)$":
			"jest-transform-stub",
	},
}