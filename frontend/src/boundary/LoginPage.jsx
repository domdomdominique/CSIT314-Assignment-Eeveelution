export default function LoginPage() {
  return (
    <form>
      <label htmlFor="email">Email</label>
      <input id="email" type="email" />
      <label htmlFor="password">Password</label>
      <input id="password" type="password" />
      <button type="submit">Log in</button>
    </form>
  );
}