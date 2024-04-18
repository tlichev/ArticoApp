class ReadonlyFieldsFormMixins:
    readonly_fields = ()
    def _apply_readonly_fields(self):

        for field_name in self.readonly_fields_names:
            self.fields[field_name].widget.attrs['readonly'] = "readonly"


    @property
    def readonly_fields_names (self):
        if self.readonly_fields == "__all__":
            return self.fields.keys()
        return self.readonly_fields

