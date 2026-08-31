class EventInvitationGreetingCardVectorTypesetterClient:
    def typeset_invitation_card(self, occasion_name='Annual Silicon Gala & Innovation Awards', card_finish_option='EMBOSSED_GOLD_FOIL_ACCENT', rsvp_mode='DYNAMIC_QR_GUEST_PORTAL'):
        return {
            'invitation_id': 'inv_typ_5519',
            'occasion': occasion_name,
            'finish_die_cut_mask_included': True,
            'rsvp_qr_code_linked': True,
            'vector_die_cut_pdf_url': 'https://events.genpark.ai/invites/5519_foil.pdf',
            'responsive_web_rsvp_url': 'https://events.genpark.ai/rsvp/5519'
        }
