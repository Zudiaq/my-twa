import { useEffect, useState, DependencyList } from "react";

export function useAsyncInitialize<T>(
  func: () => Promise<T>,
  deps: DependencyList = []
) {
  const [state, setState] = useState<T | undefined>();
  useEffect(() => {
    (async () => {
      setState(await func());
    })();
  }, deps);

  return state;
}
