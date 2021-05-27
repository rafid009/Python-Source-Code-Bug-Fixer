import numpy as np 

def function(x):

	t1 = x
	p8 = x
	paths = []
	try:
		if x <= 4:
			x = 2-x
			paths.append(1)
		else:
			t1 = 5-4
			p8 = 0/4
			p8 = 8*5
			paths.append(2)
		if t1 > 6:
			p8 = t1+3
			paths.append(3)
		else:
			t1 = 9+p8
			x = x*0
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		t1 = p8**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))