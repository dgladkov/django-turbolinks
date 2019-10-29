
class TurbolinksDjango {
    static form_submit(event) {
        var form_data = $(this).serialize();
        var button = event.originalEvent.explicitOriginalTarget;

        if (button.name) {
            // jQuery.serialize ignores <button> values and
            // doesn't include them in the parameters which breaks
            // the wizard. So we add it ourselves.
            form_data += "&" + button.name + "=" + button.value;
        }

        var out = $.post({
            url:"",
            data: form_data,
            headers : {
                "Turbolinks-Referrer": document.URL
            }
        });

        out.done((data, textStatus, jqXhr) => {
            if (jqXhr.status == 200 && jqXhr.getResponseHeader("content-type") == "text/html; charset=utf-8") {
                /* Here, we are handling an invalid form
                which means the server sent us HTML. Tell Turbolinks
                to render it.*/
                TurbolinksDjango.render_html(data);
            }
        })
        return false;
    }

    static render_html(html) {
        /* This will break for Turbolinks >= 5.3.0 because we use non public API.*/
        let controller = Turbolinks.controller;
        let currentSnapshot = Turbolinks.Snapshot.fromHTMLElement(document.documentElement);
        let nextSnapshot = Turbolinks.Snapshot.fromHTMLString(html);
        let renderer = new Turbolinks.SnapshotRenderer(currentSnapshot, nextSnapshot, false);
        renderer.mergeHead();
        renderer.replaceBody();
        renderer.focusFirstAutofocusableElement();
        controller.notifyApplicationAfterPageLoad();
    }

    static install_form_submit_handler() {
        document.addEventListener("turbolinks:load", (event) => {
            $("form[data-use-turbolinks='true']").submit(TurbolinksDjango.form_submit);
        });
    }
}
