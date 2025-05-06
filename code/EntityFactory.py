from code.Background import Background
from code.Entity import Entity

class EntityFactory:
    @staticmethod
    def get_entity(self, entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(11):
                    list_bg.append(Background(name=f'Level1Bg{i}', position=(0, 0)))
                return list_bg
