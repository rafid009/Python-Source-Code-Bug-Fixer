import numpy as np 

def function(x):

	t3 = x
	m0 = 7
	paths = []
	try:
		if m0 <= 1:
			t3 = 3/7
			x = x+t3
			x = x*9
			paths.append(1)
		else:
			t3 = t3/6
			paths.append(2)
		if t3 >= 6:
			t3 = t3*0
			t3 = x+x
			x = x/3
			paths.append(3)
		else:
			t3 = 4-6
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		m0 = t3**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))