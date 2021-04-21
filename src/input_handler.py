from typing import Optional

import tcod.event

from actions import Action, EscapeAction, MovementAction

class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        if key == tcod.event.K_UP or key == tcod.event.K_8:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN or key == tcod.event.K_2:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT or key == tcod.event.K_KP_4:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT or key == tcod.event.K_6:
            action = MovementAction(dx=1, dy=0)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        # No valid key pressed
        return action
