const copyButton = document.querySelector("#copyButton");
const code = `<!DOCTYPE html>\n<html lang="zh-Hant">\n  <body>\n    <h1>Hello, web!</h1>\n    <p>我的第一個網頁。</p>\n  </body>\n</html>`;

copyButton.addEventListener("click", async () => {
  await navigator.clipboard.writeText(code);
  copyButton.textContent = "已複製 ✓";
  window.setTimeout(() => { copyButton.textContent = "複製程式碼"; }, 1600);
});

document.querySelectorAll(".quiz-options button").forEach((button) => {
  button.addEventListener("click", () => {
    const result = document.querySelector("#quizResult");
    document.querySelectorAll(".quiz-options button").forEach((item) => item.classList.remove("selected"));
    button.classList.add("selected");
    const correct = button.dataset.answer === "correct";
    result.textContent = correct ? "答對了！<h1> 是頁面中最重要的標題。" : "再想一下：title 是瀏覽器分頁名稱，header 是內容區塊。";
    if (correct) {
      document.querySelector("#progressBar").style.width = "50%";
      document.querySelector("#progressText").textContent = "50%";
    }
  });
});

document.querySelectorAll(".lesson-link").forEach((link) => {
  link.addEventListener("click", () => {
    document.querySelectorAll(".lesson-link").forEach((item) => item.classList.remove("active"));
    link.classList.add("active");
    document.querySelector("#sidebar").classList.remove("open");
  });
});

document.querySelector("#menuButton").addEventListener("click", () => {
  document.querySelector("#sidebar").classList.toggle("open");
});
