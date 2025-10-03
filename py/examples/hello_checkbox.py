from h2o_wave import main, app, Q, ui

@app('/hello_checkbox')
async def serve(q: Q):
    if not q.client.initialized:
        q.page['form'] = ui.form_card(
            box='1 1 2 2',
            items=[
                ui.checkbox(name='like_wave', label='I like H2O Wave!'),
                ui.button(name='submit', label='Submit', primary=True),
            ]
        )
        q.client.initialized = True
        await q.page.save()
        return

    if q.args.submit:
        liked = 'Yes 🎉' if q.args.like_wave else 'No 😢'
        q.page['result'] = ui.markdown_card(
            box='1 3 2 2',
            title='Result',
            content=f'**Do you like Wave?** {liked}'
        )
        await q.page.save()
