Population Growth example:

$$ N'(t) = r \cdot N(t) => N(t) = N_0 \cdot e^{rt} $$

**Deriving a Model**

$$ N(t + \Delta{t}) - N(t) = \bar{b} \cdot N(t) - \bar{d} \cdot N(t) $$

$$ b = \frac{\bar{b}}{\Delta{t}}, \quad  d = \frac{\bar{d}}{\Delta{t}}, \quad r = b - d $$

$$ N(t + \Delta{t}) = N(t) + \Delta{t} \cdot r \cdot N(t) $$

Initial condition: $N(0) = N_0$. Then

$$ N(\Delta{t}) = N_0 + \Delta{t} \cdot r \cdot N_0 $$

$$ N((k + 1)\Delta{t}) = N(k \cdot \Delta{t}) + \Delta{t} \cdot r \cdot N(k \cdot \Delta{t}) $$

$$ N((k+ 1)\Delta{t}) = N(k \cdot \Delta{t})(1+ \Delta{t} \cdot r) $$

$$ N((k+ 1)\Delta{t}) = N((k -1) \cdot \Delta{t}) \cdot (1 + \Delta{t} \cdot r)^2 $$

$$ N((k+ 1)\Delta{t}) = N_0 (1 + \Delta{t} \cdot r)^{k+1} $$

$$ \lim_{{\Delta t \to 0}} \frac{{N(t + \Delta t) - N(t)}}{{\Delta t}} = r \cdot N(t)$$

$$ \frac{{dN(t)}}{{dt}} = r \cdot N(t) $$

$\textit{r}$ could change with time due to, e.g., seasonal changes or more permanent environmental changes.

$$ \frac{{dN}}{{dt}} = r \cdot N $$ 

$$ \int_{N_0}^{N} \frac{dN}{N} = \int_{0}^{t} r \cdot dt $$

$$ ln N - ln N_0 = \int_{0}^{t} r \cdot dt $$

$$ N = N_0 e^{\int_{0}^{t} r \cdot dt} $$

If $\textit{r}$ is constant:

$$ N = N_0 \cdot e^{r \cdot t} $$


