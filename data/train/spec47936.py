import numpy as np 

def function(x):

	h8 = 2
	t5 = 4
	paths = []
	try:
		if t5 < 8:
			t5 = 3*0
			h8 = 9+h8
			paths.append(1)
		else:
			h8 = h8*1
			paths.append(2)
		if t5 <= 7:
			h8 = x+t5
			paths.append(3)
		else:
			h8 = h8*8
			h8 = 9/9
			t5 = 5+t5
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		x = h8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))