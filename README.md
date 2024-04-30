### Auto generate models

Download the swagger file from the HelloAsso API documentation. It use an old swagger 2 version. You need to convert it to OpenAPI 3.0.0 version. You can use the online tool [Swagger Editor](https://editor.swagger.io/).

Then you can use the `datamodel-codegen` tool to generate the models:

```bash
datamodel-codegen --input HelloAssoV5OpenAPI.json --output HelloAssoAPIWrapper
```

### Notification result webhooks

You should configure a webhook to receive the notification results.
HelloAsso will make a POST request to the URL you provided with a JSON payload corresponding to a `NotificationResultContent` object.
