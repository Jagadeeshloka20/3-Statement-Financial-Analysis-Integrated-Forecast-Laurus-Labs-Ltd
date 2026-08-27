import numpy as np, pandas as pd

def build_model(revenue0=6813, growth=(.10,.10,.09,.09,.08), margin=.27, tax=.25,
                da_pct=.045, capex_pct=.12, dso=110, inv_days=125, dpo=60, payout=.15):
    rev=[]; p=revenue0
    for g in growth: p*=1+g; rev.append(p)
    rev=np.array(rev)
    ebitda=rev*margin; da=rev*da_pct; ebit=ebitda-da
    tax_exp=ebit*tax; pat=ebit-tax_exp
    ar=rev*dso/365; inv=rev*inv_days/365; ap=rev*dpo/365
    nwc=ar+inv-ap; dnwc=np.r_[nwc[0]-revenue0*(dso+inv_days-dpo)/365,np.diff(nwc)]
    cfo=pat+da-dnwc; capex=rev*capex_pct; fcf=cfo-capex
    dividends=pat*payout; cash=np.cumsum(fcf-dividends)+100
    return pd.DataFrame({"year":range(2027,2032),"revenue":rev,"EBITDA":ebitda,"PAT":pat,
                         "AR":ar,"Inventory":inv,"AP":ap,"Change_NWC":dnwc,"CFO":cfo,
                         "CapEx":capex,"FCF":fcf,"Dividends":dividends,"EndingCash":cash})
if __name__=="__main__": print(build_model().to_string(index=False))
