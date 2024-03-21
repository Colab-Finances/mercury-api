import {
  Outlet,
  RouterProvider,
  createMemoryHistory,
  createRootRoute,
  createRoute,
  createRouter,
} from '@tanstack/react-router'
import { act, render } from '@testing-library/react'
import React from 'react'

function createTestRouter(component: () => JSX.Element) {
  const rootRoute = createRootRoute({
    component: Outlet,
  })

  const componentRoute = createRoute({
    getParentRoute: () => rootRoute,
    path: '/',
    component,
  })

  return createRouter({
    routeTree: rootRoute.addChildren([componentRoute]),
    history: createMemoryHistory(),
  })
}

export async function renderWithContext(component: () => JSX.Element) {
  const router = createTestRouter(component)
  return act(() => {
    render(<RouterProvider router={router} />)
  })
}
