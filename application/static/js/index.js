$(document).ready(function () {
  sel_status = $("#select_status");
  let row_id;
  let row_status;

  $("#SP_Table thead th").each(function () {
    var title = $(this).text();
    $(this).html('<input type="text" placeholder="Search ' + title + '" />');
  });

  console.log("***Table***");
  const url = "api/cards/";
  console.log(url);
  let table = $("#SP_Table").DataTable({
    ajax: {
      url: url,
      dataSrc: "",
    },
    columns: [
      { data: "id", visible: false },
      { data: "series" },
      { data: "number" },
      { data: "date_issue" },
      { data: "date_expiration" },
      { data: "limit" },
      { data: "status" },
    ],
    DisplayLength: 10,
    processing: true,
    lengthMenu: [
      [10, 15, 20, -1],
      [10, 15, 20, "Все"],
    ],
    createdRow: function (row, data) {
      if (new Date(data.date_expiration) <= new Date()) {
        $("td", row).eq(5).html("expired");
        $("td", row).eq(5).addClass("redcode pulse");
      } else {
        if (data.status == "not_activated") {
          $("td", row).eq(5).addClass("orangecode pulse");
        }
        if (data.status == "expired") {
          $("td", row).eq(5).addClass("redcode pulse");
        }
        if (data.status == "active") {
          $("td", row).eq(5).addClass("greencode pulse");
        }
      }
    },
    initComplete: function () {
      this.api()
        .columns()
        .every(function () {
          var that = this;

          $("input", this.header()).on("keyup change clear", function () {
            if (that.search() !== this.value) {
              that.search(this.value).draw();
            }
          });
        });
    },
  });

  $("#SP_Table tbody").on("click", "tr", function () {
    if ($(this).hasClass("selected")) {
      $(this).removeClass("selected");
    } else {
      table.$("tr.selected").removeClass("selected");
      $(this).addClass("selected");
      var data = table.row(table.$("tr.selected")).data();
      console.log(data);
      row_id = data["id"];
      row_status = data["status"];
    }
  });

  function fill_status() {
    sel_status.empty();
    sel_status.append(`<option value="active">активировать</option>`);
    sel_status.append(`<option value="not_activated">деактивировать</option>`);
    sel_status.val(row_status);
  }

  $("#EditTaskButton").on("click", function () {
    if (table.row(table.$("tr.selected")).index() != undefined) {
      fill_status();
      $("#edit-create-norm-title").html("Изменение статуса");
      $("#CreateTaskOkButton").html("Редактировать");
      $("#CreatEditTaskModal").fadeIn();
    }
  });

  $("#StatButton").on("click", function () {
    if (table.row(table.$("tr.selected")).index() != undefined) {
      $("#StatTaskModal").fadeIn();
      $("#list_trans").empty();
      $("#list_trans").append(
        `<thead>
            <tr>
                <th scope="col">Дата</th>
                <th scope="col">Тип</th>
                <th scope="col">Сумма</th>
            </tr>
        </thead>`
      );
      $.ajax({
        type: "GET",
        url: "api/transactions/?card=" + row_id,
        success: function (response) {
          for (i = 0; i < response.length; i++) {
            console.log(response[i]);
            $("#list_trans").append(
              `<tr><td>${response[i].date}</td><td>${response[i].type}</td><td>${response[i].sum}</td></tr>`
            );
          }
        },
      });
    }
  });

  $("#StatTaskClose1").on("click", function () {
    $("#StatTaskModal").fadeOut();
  });

  $("#StatTaskClose2").on("click", function () {
    $("#StatTaskModal").fadeOut();
  });

  $("#CeateTaskClose1").on("click", function () {
    $("#CreatEditTaskModal").fadeOut();
  });

  $("#CeateTaskClose2").on("click", function () {
    $("#CreatEditTaskModal").fadeOut();
  });

  $("#CreateTaskOkButton").on("click", function () {
    csrftoken = window.CSRF_TOKEN;
    function csrfSafeMethod(method) {
      // these HTTP methods do not require CSRF protection
      return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
    }
    $.ajaxSetup({
      beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      },
    });

    const new_status = {
      status: sel_status.val(),
    };

    $.ajax({
      type: "PATCH",
      url: "api/cards/" + row_id + "/",
      data: JSON.stringify(new_status),
      contentType: "application/json",
      dataType: "json",
      success: function (data) {
        table.ajax.reload();
        $("#CreatEditTaskModal").fadeOut();
      },
      error: function (errMsg) {
        alert(`Ошибка при редактировании карты\n${JSON.stringify(errMsg)}`);
        console.log(JSON.stringify(errMsg));
      },
    });
  });

  $("#DeleteTaskButton").on("click", function () {
    $.ajax({
      type: "DELETE",
      url: "api/cards/" + row_id + "/",
      contentType: "application/json",
      dataType: "json",
      success: function (data) {
        table.ajax.reload();
      },
      error: function (errMsg) {
        alert(`Ошибка при удалении карты\n${JSON.stringify(errMsg)}`);
        console.log(JSON.stringify(errMsg));
      },
    });
  });
});
