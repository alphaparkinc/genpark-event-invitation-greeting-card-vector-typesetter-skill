from client import EventInvitationGreetingCardVectorTypesetterClient

def main():
    client = EventInvitationGreetingCardVectorTypesetterClient()
    res = client.typeset_invitation_card('Executive Leadership Retreat 2026', 'METALLIC_COPPER_ACCENT')
    print('Invitation Card Typesetter: ' + res['invitation_id'] + ' (' + res['occasion'] + ')')
    print('Die-Cut Mask: ' + str(res['finish_die_cut_mask_included']) + ' | RSVP QR: ' + str(res['rsvp_qr_code_linked']))
    print('Vector PDF: ' + res['vector_die_cut_pdf_url'])
    print('Web RSVP: ' + res['responsive_web_rsvp_url'])

if __name__ == '__main__':
    main()
