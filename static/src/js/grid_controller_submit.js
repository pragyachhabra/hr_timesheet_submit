odoo.define('hr_timesheet_submit.GridControllerSubmit', function (require) {
"use strict";

var GridController = require('web_grid.GridController');

GridController.include({

    /*
     *  @override
    */

    init: function (parent, model, renderer, params) {
        this._super.apply(this, arguments);
    },

    renderButtons: function ($node) {
        this._super.apply(this, arguments);
        this.$buttons.on('click', '.grid_button_submit', this._onCheckSubmitted.bind(this));
    },

    _updateButtons: function () {
        var self = this;
        if (this.$buttons) {
            var grid_button_submit = self.$buttons.find('.grid_button_submit');
            grid_button_submit["0"].style.display = "none";
            if (this.__parentedParent.active_view.fields_view.name == 'account.analytic.line.grid.project')
            {
                if (this.model._gridData.grid)
                {
                   var grid = this.model._gridData.grid;
                }
                else if (this.model._gridData["0"].grid)
                {
                    var grid = this.model._gridData["0"].grid;
                }
                if (grid)
                {
                    var allsubm = false;
                    for (var i = 0; i < grid.length; i++)
                    {
                       var row = grid[i];
                       for (var y = 0; y < row.length; y++)
                       {
                           var cell = row[y];
                           if (cell.size) {
                               this._rpc({
                                   model: 'account.analytic.line',
                                   method: 'check_submitted_validated',
                                   args: [cell.domain]
                               }).done(function (value) {
                                   if (value)
                                   {
                                       allsubm = true;
                                       grid_button_submit["0"].style.display = "inline";
                                       grid_button_submit["0"].className += " active";
                                   }
                               })
                           }
                       }
                    }
                   if (!allsubm)
                   {
                       grid_button_submit["0"].style.display = "none";
                   }
                }
            }
        }
        this._super.apply(this, arguments);

    },

    //--------------------------------------------------------------------------
    // Handlers
    //--------------------------------------------------------------------------

    /**
     * @private
     * @param {MouseEvent} event
     */
    _onCheckSubmitted: function (event) {
        event.preventDefault();
        if (this.model._gridData.grid)
        {
           var grid = this.model._gridData.grid; 
        }
        else if (this.model._gridData["0"].grid)
        {
            var grid = this.model._gridData["0"].grid;
        }
        
        if (grid)
        {
            for (var i = 0; i < grid.length; i++)
            {
                var row = grid[i];
                for (var y = 0; y < row.length; y++)
                {
                    var cell = row[y];
                    if (cell.size)
                    {
                        this._rpc({
                            model: 'account.analytic.line',
                            method: 'mark_submitted',
                            args: [cell.domain]
                        });
                    }

                }
            }
        }
        event.target.style.display = "none"
    }
});

});
