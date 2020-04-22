//
// Sauvegarde d'un dossier / analyse
//

export default function savePageAs(fileName) {
  if (!fileName) {
    fileName = location.href.toString();
  }
  var X = new XMLHttpRequest(),
    data = "";
  X.open("GET", fileName, false);
  X.send("");
  data = X.responseText;
  return window.open(
    "data:x-application/external;charset=utf-8," + escape(data)
  );
}
