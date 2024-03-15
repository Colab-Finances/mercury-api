/* prettier-ignore-start */

/* eslint-disable */

// @ts-nocheck

// noinspection JSUnusedGlobalSymbols

// This file is auto-generated by TanStack Router

// Import Routes

import { Route as rootRoute } from './sections/shared/routes/__root'
import { Route as LoginImport } from './sections/auth/routes/login'
import { Route as RegisterImport } from './sections/users/routes/register'
import { Route as LayoutImport } from './sections/shared/routes/_layout'
import { Route as DashboardImport } from './sections/dashboard/routes'

// Create/Update Routes

const RegisterRoute = RegisterImport.update({
  path: '/register',
  getParentRoute: () => rootRoute,
} as any)

const LoginRoute = LoginImport.update({
  path: '/login',
  getParentRoute: () => rootRoute,
} as any)

const LayoutRoute = LayoutImport.update({
  id: '/_layout',
  getParentRoute: () => rootRoute,
} as any)

const DashboardRoute = DashboardImport.update({
  path: '/',
  getParentRoute: () => LayoutRoute,
} as any)

// Register the router instance for type safety
declare module '@tanstack/react-router' {
  interface FileRoutesByPath {
    '/_layout': {
      preLoaderRoute: typeof LayoutImport
      parentRoute: typeof rootRoute
    }
    '/': {
      preLoaderRoute: typeof DashboardRoute
      parentRoute: typeof LayoutImport
    }
    '/login': {
      preLoaderRoute: typeof LoginImport
      parentRoute: typeof rootRoute
    }
    '/register': {
      preLoaderRoute: typeof RegisterImport
      parentRoute: typeof rootRoute
    }
  }
}

// Create and export the route tree

export const routeTree = rootRoute.addChildren([
  LayoutRoute.addChildren([DashboardRoute]),
  LoginRoute,
  RegisterRoute,
])

/* prettier-ignore-end */
