<odoo>
    <data>
        <record id="view_partner_form_inherit" model="ir.ui.view">
        <field name="name">res.partner.form.inherit</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="base.view_partner_form"/>
        <field name="arch" type="xml">
                 <xpath expr="//field[@name='mobile']" position='after'>
                        <field name="company_name"/>
                        <field name="chinese_name"/>
                </xpath>


        </field>
        </record>
    </data>
</odoo>

