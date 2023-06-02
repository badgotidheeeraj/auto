function processData(data) {
  var array = data.Type_id;
  console.log(array);
  return [
    MLA_(array),
    Chicago_(array),
    Harvarde_(array),
    Vancouver_(array),
    getCheckboxValue(array),
  ];
}

// APA
function getCheckboxValue(data) {
  var myArray = data;
  var checkbox = document.getElementById("myCheckbox");
  var g = myArray.includes("APA");
  var i = checkbox.checked;
  console.log(i);
  if (g == i) {
    checkbox.checked = true;
  } else {
    checkbox.checked = false;
  }
}

// Harvard
function Harvarde_(data) {
  var myArray = data;
  var checkbox = document.getElementById("Harvarde");
  var g = myArray.includes("Harvard");
  var i = checkbox.checked;
  if (g == i) {
    checkbox.checked = true;
  } else {
    checkbox.checked = false;
  }
}
//Chicago
function Chicago_(data) {
  var myArray = data;
  var checkbox = document.getElementById("Chicago");
  var g = myArray.includes("Chicago");
  var i = checkbox.checked;
  if (g == i) {
    checkbox.checked = true;
  } else {
    checkbox.checked = false;
  }
}
// Vancouver
function Vancouver_(data) {
  var myArray = data;
  var checkbox = document.getElementById("Vancouver");
  var g = myArray.includes("Vancouver");
  var i = checkbox.checked;
  if (g == i) {
    checkbox.checked = true;
  } else {
    checkbox.checked = false;
  }
}
// MLA
function MLA_(data) {
  var myArray = data;
  var checkbox = document.getElementById("MLA");
  var g = myArray.includes("MLA");
  var i = checkbox.checked;
  if (g == i) {
    checkbox.checked = true;
  } else {
    checkbox.checked = false;
  }
}

MLA_();
Chicago_();
Harvarde_();
Vancouver_();
getCheckboxValue();
