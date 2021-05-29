import numpy as np 

def function(x):

	m7 = x
	w5 = 2
	paths = []
	try:
		if x < 7:
			w5 = w5*0
			x = 4+7
			paths.append(1)
		else:
			x = x*7
			x = m7+7
			paths.append(2)
		if m7 < 5:
			w5 = w5*2
			paths.append(3)
		else:
			x = x/6
			x = m7+3
			m7 = 5/m7
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		w5 = m7**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))