
--  ACTUALIZAR PRECIO PRODUCTO
DELIMITER //
CREATE TRIGGER actualizarPrecioProducto
	BEFORE UPDATE ON app_producto
	FOR EACH ROW
	BEGIN
	  IF NEW.costo <> OLD.costo
		THEN
		  SET NEW.valor = (NEW.costo * 1.19)*1.35;
	  END IF ;
	END//
DELIMITER;

-- ACTUALIZAR ESTADO DE STOCK
DELIMITER //
CREATE TRIGGER actualizarEstadoStock
	BEFORE UPDATE ON app_producto
	FOR EACH ROW
	BEGIN
	  IF NEW.stock < OLD.stock_min
		THEN
		  SET NEW.estado = 'Agotado';
	  END IF ;
	END//
DELIMITER;