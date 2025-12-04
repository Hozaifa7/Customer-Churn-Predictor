from enum import Enum
from pydantic import BaseModel

class GenderEnum(str, Enum):
    male = "Male"
    female = "Female"

class YesNoEnum(str, Enum):
    yes = "Yes"
    no = "No"

class ContractEnum(str, Enum):
    month_to_month = "Month-to-month"
    one_year = "One year"
    two_year = "Two year"

class PaymentMethodEnum(str, Enum):
    electronic_check = "Electronic check"
    mailed_check = "Mailed check"
    bank_transfer = "Bank transfer (automatic)"
    credit_card = "Credit card (automatic)"

class InternetServiceEnum(str, Enum):
    dsl = "DSL"
    fiber_optic = "Fiber optic"
    no = "No"

class ZeroOneEnum(str, Enum):
    zero = "0"
    one = "1"

class MultipleLinesEnum(str, Enum):
    no_phone_service = "No phone service"
    no = "No"
    yes = "Yes"

class internalEnum(str, Enum):
    no_internet_service = "No internet service"
    no = "No"
    yes = "Yes"

class CustomerFeatures(BaseModel):
    gender: GenderEnum
    SeniorCitizen: ZeroOneEnum
    Partner: YesNoEnum
    Dependents: YesNoEnum
    tenure: int
    PhoneService: YesNoEnum
    MultipleLines: MultipleLinesEnum
    InternetService: InternetServiceEnum
    OnlineSecurity: internalEnum
    OnlineBackup: internalEnum
    DeviceProtection: internalEnum
    TechSupport: internalEnum
    StreamingTV: internalEnum
    StreamingMovies: internalEnum
    Contract: ContractEnum
    PaperlessBilling: YesNoEnum
    PaymentMethod: PaymentMethodEnum
    MonthlyCharges: float
    TotalCharges: float
